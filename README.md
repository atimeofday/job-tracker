# Personal Job Application Tracker
An interactive app I wrote to easily gather and view data about my ongoing job search

## Overview
This is a CLI tool which helps quickly track and analyze job applications, rather than recording a simple number of applications or nothing at all. The primary goal of collecting additional data is to determine which sources and methods are most effective for landing interviews, while also providing a convenient record of applications sorted by date.

## Features
- Log new job applications with key details:
  - Application date
  - Source (e.g. LinkedIn, Indeed, Company Website)
  - Type (Short or long, low or high effort)
  - Company name
- View applications filtered by:
  - Time period (current month, week, or day)
  - Source
  - Type
- CSV-format data storage for analytics, scaling, and portability

## Usage
The tracker currently provides two main commands:

`apply` - Add a new job application
- Quick, oneshot input for minimal effort and friction
- Shortens to `a` as in `a gs Company A` for "applied quickly on Glassdoor to Company A"

`ls` - List job applications with optional filters
- No filter: Shows current month's applications
- `m(onth)`: Current month
- `w(eek)`: Current week  
- `d(ay)`: Current day
- `a(ll)`: All applications
- Source/Type code: Filter by specific source or type
- `o(ptions)` or `h`: Show available source and type options

## Demo
[Screencast From 2025-02-12 10-39-12.webm](https://github.com/user-attachments/assets/84dc3427-87c5-4e28-b9a0-733919096987)
