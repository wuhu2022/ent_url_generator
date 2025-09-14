import pandas as pd
import urllib.parse
import os
import sys
import argparse

def extract_names_and_generate_urls(excel_file_path, scopus_output_file='scopus_search_urls.txt', orcid_output_file='orcid_search_urls.txt'):
    """
    Extract First_Name and Last_Name from Excel file and generate Scopus and ORCID search URLs
    """
    try:
        # Read the Excel file
        df = pd.read_excel(excel_file_path)
        
        print(f"Generating URLs from: {excel_file_path}")
        print("Generating Scopus and ORCID search URLs...")
        
        # Find the correct columns
        first_name_col = None
        last_name_col = None
        
        for col in df.columns:
            if 'first_name' in col.lower() or 'firstname' in col.lower():
                first_name_col = col
            elif 'last_name' in col.lower() or 'lastname' in col.lower():
                last_name_col = col
        
        if not first_name_col or not last_name_col:
            print("Could not find First_Name and Last_Name columns automatically.")
            return
        
        print(f"Using columns: {first_name_col} and {last_name_col}")
        
        # Generate Scopus URLs
        scopus_urls = []
        orcid_urls = []
        for index, row in df.iterrows():
            first_name = str(row[first_name_col]).strip() if pd.notna(row[first_name_col]) else ""
            last_name = str(row[last_name_col]).strip() if pd.notna(row[last_name_col]) else ""
            
            if first_name and last_name and first_name != 'nan' and last_name != 'nan':
                # Generate Scopus search URL using the provided template
                scopus_url = f"https://www.scopus.com/results/authorNamesList.uri?sort=count-f&src=al&sid=019d6a5f04c0d727df785a0d224cdb9a&sot=al&sdt=al&sl=42&s=AUTHLASTNAME%28{last_name}%29+AND+AUTHFIRST%28{first_name}%29&st1={last_name}&st2={first_name}&orcidId=&selectionPageSearch=anl&reselectAuthor=false&activeFlag=true&showDocument=false&resultsPerPage=20&offset=1&jtp=false&currentPage=1&previousSelectionCount=0&tooManySelections=false&previousResultCount=0&authSubject=LFSC&authSubject=HLSC&authSubject=PHSC&authSubject=SOSC&exactAuthorSearch=false&showFullList=false&authorPreferredName=&origin=searchauthorfreelookup&affiliationId=&txGid=d17770acfb76819559b5a71a877fb194"
                orcid_url = f"https://orcid.org/orcid-search/search?searchQuery={urllib.parse.quote(f'{first_name} {last_name}')}"
                scopus_urls.append(scopus_url)
                orcid_urls.append(orcid_url)
                print(f"Row {index + 1}: {first_name} {last_name} -> Scopus and ORCID URL generated")
        
        # Save URLs to files
        with open(scopus_output_file, 'w', encoding='utf-8') as f:
            for url in scopus_urls:
                f.write(url + '\n')
        
        with open(orcid_output_file, 'w', encoding='utf-8') as f:
            for url in orcid_urls:
                f.write(url + '\n')

        print(f"\nGenerated {len(scopus_urls)} Scopus URLs and saved to '{scopus_output_file}'")
        print(f"Generated {len(orcid_urls)} ORCID URLs and saved to '{orcid_output_file}'")
        
        # Show a few examples
        print("\nFirst 5 Scopus URLs:")
        for i, url in enumerate(scopus_urls[:5]):
            print(f"{i+1}. {url}")
        
        print("\nFirst 5 ORCID URLs:")
        for i, url in enumerate(orcid_urls[:5]):
            print(f"{i+1}. {url}")
        
        return scopus_urls, orcid_urls
        
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        print("Make sure you have pandas and openpyxl installed:")
        print("pip install pandas openpyxl")
        return None

def main():
    """
    Main function to handle command line arguments and run the URL extraction
    """
    parser = argparse.ArgumentParser(description='Extract names from Excel file and generate Scopus and ORCID search URLs')
    parser.add_argument('excel_file', help='Path to the Excel file containing First_Name and Last_Name columns')
    parser.add_argument('--output-scopus', default='scopus_search_urls.txt', 
                       help='Output file for Scopus URLs (default: scopus_search_urls.txt)')
    parser.add_argument('--output-orcid', default='orcid_search_urls.txt', 
                       help='Output file for ORCID URLs (default: orcid_search_urls.txt)')
    
    args = parser.parse_args()
    
    # Check if file exists
    if not os.path.exists(args.excel_file):
        print(f"Error: File '{args.excel_file}' not found.")
        sys.exit(1)
    
    # Check if file is Excel
    if not args.excel_file.lower().endswith(('.xlsx', '.xls')):
        print(f"Error: File '{args.excel_file}' is not an Excel file (.xlsx or .xls)")
        sys.exit(1)
    
    print(f"Processing Excel file: {args.excel_file}")
    print(f"Scopus URLs will be saved to: {args.output_scopus}")
    print(f"ORCID URLs will be saved to: {args.output_orcid}")
    print("-" * 50)
    
    # Run the extraction
    result = extract_names_and_generate_urls(args.excel_file, args.output_scopus, args.output_orcid)
    
    if result:
        scopus_urls, orcid_urls = result
        print(f"\n✅ Successfully generated {len(scopus_urls)} Scopus URLs and {len(orcid_urls)} ORCID URLs!")
    else:
        print("\n❌ Failed to generate URLs.")
        sys.exit(1)

if __name__ == "__main__":
    main()
