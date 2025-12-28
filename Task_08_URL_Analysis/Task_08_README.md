#Task 8 – URL Component Analysis and Robots.txt Permission Evaluation


Objective This task explores the fundamental components of web architecture and crawling ethics in Information Retrieval. The goal is to build a robust parser that decomposes complex URLs and interprets the robots.txt protocol to determine data harvesting constraints.

Dataset The analysis was performed on a set of live, diverse URLs representing different organizational structures:

Media: CNN (Global news platform)

Museum/Research: Natural History Museum (UK-based academic/public site)

Academic: University of Haifa (Israeli academic subdomain)

URL Component Extraction The system identifies and extracts the following seven logical components from any given input URL:

TLD: Top-Level Domain (with support for multi-part suffixes like .ac.uk and .ac.il)

Domain: The registered organizational name

Subdomain: Secondary domains preceding the main name

Path: The hierarchical directory structure

File Name: The specific resource or document being accessed

Query Parameters: Key-value pairs used for dynamic content filtering

Port: Explicit or scheme-default communication ports

Robots.txt Analysis The system performs a live fetch of the robots.txt file from the host server. It simulates a standard web crawler using custom headers to avoid HTTP 403 (Forbidden) errors. The following data is parsed:

Disallowed URLs: All relative paths under the Disallow directive are extracted and concatenated with the host URL to create absolute links.

User-agent Restrictions: Specific bots and crawlers that are explicitly mentioned in the exclusion list.

Crawl-delay: Detection of server-requested wait times between requests to manage server load.

Implementation Details

TLD Logic: Implemented a conditional check for Second-Level Domains (SLDs) to prevent misclassifying .ac or .co as the primary domain.

Standardization: Utilized urllib.parse for industry-standard URI decomposition.

Normalization: Applied case-insensitive matching for robots.txt directives to ensure compatibility with varied server configurations.

Observations

Major media outlets like CNN have extensive lists of disallowed bots, specifically targeting AI training crawlers.

Academic and research institutions often implement a Crawl-delay (e.g., 8 seconds) to protect server resources.

The system successfully reconstructs full access-restricted paths, which is critical for the "Frontier" management of a search engine crawler.

Technologies Used

Python

urllib (Parse and Request modules)

pandas (For structured tabular analysis)

Author Yousef Shihade 
Information Retrieval Course
