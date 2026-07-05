# CRM Update Agent Architecture

CRM data hygiene agent that validates and enriches contact records, detects duplicates, logs activities automatically, maintains data quality, and syncs information across sales tools.

## Domain Tools

- **validate_records**: Validate CRM records for completeness and accuracy
- **detect_duplicates**: Detect and merge duplicate contact or account records
- **enrich_records**: Enrich CRM records with external data sources
- **auto_log_activity**: Automatically log email and calendar activities to CRM
- **sync_tools**: Sync CRM data with connected sales tools