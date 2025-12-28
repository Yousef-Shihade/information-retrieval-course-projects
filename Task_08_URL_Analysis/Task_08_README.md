Task 8 – URL Component Analysis and Robots.txt Permission Evaluation
Objective

This task explores the fundamental components of web architecture and crawling ethics in Information Retrieval.
The goal is to analyze complex URLs by decomposing them into logical components and to evaluate robots.txt
policies in order to determine crawler access restrictions.

Dataset

The analysis was performed on a set of live and diverse URLs, representing different organizational structures:

Media: CNN (global news platform)

Museum / Research: Natural History Museum (UK-based academic and public institution)

Academic: University of Haifa (Israeli academic subdomain)

Each URL reflects real-world complexity, including subdomains, paths, parameters, and access rules.

URL Component Extraction

For every input URL, the system extracts seven logical components:

TLD: Top-Level Domain

Supports multi-part suffixes such as .ac.uk and .ac.il

Domain: The registered organizational name

Subdomain: Any secondary domains preceding the main domain

Path: Hierarchical directory structure

File Name: The specific resource being accessed

Query Parameters: Key–value pairs for dynamic content filtering

Port: Explicit ports or scheme-default ports

Robots.txt Analysis

For each host, the system performs a live fetch of the robots.txt file and simulates a standard web crawler.
Custom HTTP headers are used to avoid 403 Forbidden responses.

The following directives are parsed:

Disallowed URLs

All paths under Disallow are extracted

Relative paths are converted into absolute URLs

User-agent Restrictions

Identification of specific crawlers or bots explicitly mentioned

Crawl-delay

Detection of server-requested delays between crawl requests

Implementation Details

TLD Logic

Conditional handling of Second-Level Domains (SLDs) to avoid misclassification
(e.g., preventing .ac or .co from being treated as primary domains)

Standardization

URL parsing implemented using urllib.parse

Normalization

Case-insensitive matching for robots.txt directives to ensure robustness across servers

Observations

Major media websites (e.g., CNN) maintain extensive bot exclusion lists, often targeting AI training crawlers.

Academic and research institutions frequently define a crawl-delay (e.g., 8 seconds) to protect server resources.

The system successfully reconstructs full restricted URLs, a critical capability for crawler frontier management in search engines.

Technologies Used

Python

urllib (parse and request modules)

pandas

Author

Yousef Shihade
Information Retrieval Course
