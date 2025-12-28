# Task 8 - Yousef Shihade 

import urllib.parse
import urllib.request
import pandas as pd

# URLs 
urls = [
    "https://edition.cnn.com/2025/12/22/media/60-minutes-cecot-bari-weiss-canada-global-tv?iid=cnn_buildContentRecirc_end_recirc&recs_exp=most-popular-article-end&tenant_id=popular.en",
    "https://www.nhm.ac.uk/visit/exhibitions/wildlife-photographer-of-the-year.html",
    "https://is-web.hevra.haifa.ac.il/images/2025_SEM._aa.pdf"
]

def parse_url(url):
    """Extract URL components with improved TLD handling"""
    parsed = urllib.parse.urlparse(url)
    netloc_parts = parsed.netloc.split('.')
    
    # Handle multi-part TLDs like .ac.uk or .ac.il
    if len(netloc_parts) > 2 and netloc_parts[-2] in ['com', 'ac', 'co', 'org', 'gov', 'net', 'edu']:
        tld = '.'.join(netloc_parts[-2:])
        domain = netloc_parts[-3]
        subdomain = '.'.join(netloc_parts[:-3]) if len(netloc_parts) > 3 else ''
    else:
        tld = netloc_parts[-1] if netloc_parts else ''
        domain = netloc_parts[-2] if len(netloc_parts) > 1 else ''
        subdomain = '.'.join(netloc_parts[:-2]) if len(netloc_parts) > 2 else ''
    
    #  path and filename
    path = parsed.path
    file_name = path.split('/')[-1] if path and path != '/' else ''
    
    #  query parameters
    query_params = dict(urllib.parse.parse_qsl(parsed.query))
    
    # Port - show explicit port or default for scheme
    port = parsed.port if parsed.port else ''
    
    return {
        'URL': url,
        'TLD': tld,
        'Domain': domain,
        'Subdomain': subdomain,
        'Path': path,
        'File Name': file_name,
        'Query Parameters': query_params,
        'Port': port
    }

def check_robots_txt(url):
    """Check robots.txt for the given URL"""
    parsed = urllib.parse.urlparse(url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    
    print(f"\n{'='*80}")
    print(f"Checking robots.txt for: {parsed.netloc}")
    print(f"robots.txt URL: {robots_url}")
    print('='*80)
    
    # Add User-Agent header to avoid being blocked
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) InformationRetrievalProject/1.0'}
    
    try:
        req = urllib.request.Request(robots_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            robots_content = response.read().decode('utf-8')
        
        print("✓ robots.txt exists!\n")
        
        # Parse robots.txt
        disallowed_paths = []
        user_agents = []
        crawl_delay = None
        
        for line in robots_content.split('\n'):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            if line.lower().startswith('user-agent:'):
                current_user_agent = line.split(':', 1)[1].strip()
                if current_user_agent != '*':
                    user_agents.append(current_user_agent)
            elif line.lower().startswith('disallow:'):
                path = line.split(':', 1)[1].strip()
                if path:
                    # B.1: Concatenate subdomain + path
                    full_url = f"{parsed.scheme}://{parsed.netloc}{path}"
                    disallowed_paths.append(full_url)
            elif line.lower().startswith('crawl-delay:'):
                crawl_delay = line.split(':', 1)[1].strip()
        
        #  results
        print("B.1 - Disallowed URLs:")
        if disallowed_paths:
            for i, path in enumerate(disallowed_paths[:10], 1):  #  first 10
                print(f"  {i}. {path}")
            if len(disallowed_paths) > 10:
                print(f"  ... and {len(disallowed_paths) - 10} more")
        else:
            print("  No disallowed paths found")
        
        print("\nB.2 - Disallowed User-agents:")
        if user_agents:
            for i, ua in enumerate(user_agents[:15], 1):  #  first 15
                print(f"  {i}. {ua}")
            if len(user_agents) > 15:
                print(f"  ... and {len(user_agents) - 15} more")
        else:
            print("  No specific user-agents disallowed (only * wildcard)")
        
        print("\nB.3 - Crawl-delay:")
        if crawl_delay:
            print(f"  Crawl-delay: {crawl_delay} seconds")
        else:
            print("  No crawl-delay specified")
            
    except urllib.error.HTTPError as e:
        print(f"✗ robots.txt not found (HTTP {e.code})")
    except Exception as e:
        print(f"✗ Error checking robots.txt: {e}")

# Main execution
print("="*80)
print("PART A: URL ANALYSIS")
print("="*80)

# Parse all URLs and create DataFrame
url_data = []
for url in urls:
    url_data.append(parse_url(url))

df = pd.DataFrame(url_data)
print("\nParsed URL Components:")
print(df.to_string(index=False))

# Part B: Check robots.txt for each URL
print("\n\n")
print("="*80)
print("PART B: ROBOTS.TXT ANALYSIS")
print("="*80)

for url in urls:
    check_robots_txt(url)
