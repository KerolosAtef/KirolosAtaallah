# Scholar Stats Auto-Update System

This document explains how the automatic Google Scholar statistics update system works.

## Overview

Your website displays live statistics from your Google Scholar profile:
- Total Citations
- Number of Publications  
- h-index
- i10-index

These stats are automatically fetched and updated **daily** by a GitHub Actions workflow.

## Update Schedule

- **Frequency**: Daily at 03:17 UTC (5:17 AM Egypt time in winter, 6:17 AM in summer)
- **Method**: Automated via GitHub Actions
- **Fallback**: If Google Scholar blocks the request, the previous cached data is kept
