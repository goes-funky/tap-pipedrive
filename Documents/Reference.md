---
title: Pipedrive
excerpt: Step by step setup guide for Pipedrive
category: 62b332e637a6a3004298b8c1
slug: pipedrive
parentDoc: 62b3332a94695c005a9703a2
---


# Pipedrive

**Integration description**

Pipedrive is a cloud-based software as a service company. It is the developer of the web application and mobile app Pipedrive, a sales customer relationship management tool.


**Company Website**

[https://www.pipedrive.com/](https://www.pipedrive.com/)

---

#  Features Supported

| Feature Name | Supported | Note |
| --- | --- | --- |
| Full Import | Yes |  |
| Incremental Import | Yes | |
| Import Empty tables | Yes |  |
| Re-import | Yes |  |
| Custom data | No |  |
| Retroactive Updating | - |  |
| Dynamic column selection | No |  |



---

# Connector

- Singer - Babelfish SDK
- Token Authentication

**Authentication**

- Authentication process relies on Api Token.
- The API token must be provided as part of the query string for all requests
- 
**Workflow**

- There are 2 different data flow for surveys at this tap.
    1. Sync Entity
        - Send a request to `/v1/{stream_name}`.
        - Parse response and generate records.
        - Sink them.
  2Sync Dynamic data. The supported entities are `activities`, `deal_details`, `delas`,`notes`,`organizations`, `persons`,`products` .
        - Send a request to `/v1/recents`.
        - Using `stream_name`, fill URL parameter named `item=stream_name` and send request.
        - Fetch data and parse response and generate records.
        - Sink them.
**Rate limits**

Rate limiting when authenticating with api_token

- Essential - 20 requests per 2 seconds per api_token
- Advanced - 40 requests per 2 seconds per api_token
- Professional - 80 requests per 2 seconds per api_token
- Enterprise - 120 requests per 2 seconds per api_token

HTTP headers and response codes

- x-ratelimit-limit - The maximum number of requests current access_token or api_token can perform per 2-second window.
- x-ratelimit-remaining - The number of requests left for the 2-second window.
- x-ratelimit-reset - The remaining window before the rate limit resets.
- x-daily-requests-left - Indicates how many requests you can still make to POST/PUT endpoints during the ongoing day (calculated in UTC). Applicable only to api_token requests.

**Pagination**

Most of the lists/item collections are paginated. The parameters that control the pagination are start and limit, indicating the desired offset and the items per page values.

The maximum limit value is 500. We use the limit 300 (For memory issues).

---

# Sync Overview

**Historical Data**

- There are not any limitation for historical data.

**Real-time data**

- Real time data is meaningless because of rate limits and recursive calls needed to fetch data. 

**Performance Consideration**

- Real time import not suggested because of recursive calls. That make the rate limit reached at a short period of time.

**Start Date Selection**

Start date can be specified.

**Multiple account selection**

There is no support for this.

**Any API feature we support**

Rate limits and rate limit reset time is being provided for each response. That information can be used to calculate next request time instead of brute force requests. But n**ot implemented yet.**

**Recommendations**

Rate limit may be higher.

---

# Schema

[**Pipedrive API v1**](https://developers.pipedrive.com/docs/api/v1)



**Streams list Link**

- Link to documentation.

## Supported Streams



| **Schema Name**                                                                                        | **Description** | **Replication Method** | **Stream Type** | **Pagination** |
|--------------------------------------------------------------------------------------------------------| -- | --- | --- | --- |
| [Activities Schema](https://developers.pipedrive.com/docs/api/v1/Activities#getActivities)              | | INCREMENTAL | Activities | Enabled by Default |
| [Deal Detail Schema](https://developers.pipedrive.com/docs/api/v1/DealFields#getDealFields)  | | INCREMENTAL | Deal Detail | Enabled by Default |
| [Deals Schema](https://developers.pipedrive.com/docs/api/v1/Deals#getDeals) | | INCREMENTAL | Deals | Enabled by Default |
| [Notes Schema](https://developers.pipedrive.com/docs/api/v1/Notes)        | | INCREMENTAL | Notes | Enabled by Default |
| [Organizations Schema](https://developers.pipedrive.com/docs/api/v1/Organizations)     | | INCREMENTAL | Organizations | Enabled by Default |
| [Persons Schema](https://developers.pipedrive.com/docs/api/v1/Persons)       | | INCREMENTAL | Persons | Enabled by Default |
| [Products Schema](https://developers.pipedrive.com/docs/api/v1/Products)      | | INCREMENTAL | Products | Enabled by Default |
| [Activity Types Schema](https://developers.pipedrive.com/docs/api/v1/ActivityTypes#getActivityTypes) | | INCREMENTAL | Activity Types  | Enabled by Default |
| [Currency Schema](https://developers.pipedrive.com/docs/api/v1/Currencies)       | | INCREMENTAL | Currency | Enabled by Default |
| [Deal Products Schema](https://developers.pipedrive.com/docs/api/v1/Deals#getDeals)  | | INCREMENTAL | Deal Products | Enabled by Default |
| [Dealflow Schema](https://developers.pipedrive.com/docs/api/v1/Deals#getDeals)       | | INCREMENTAL | Dealflow | Enabled by Default |
| [Deals Summary Schema](https://developers.pipedrive.com/docs/api/v1/Deals#getDeals)  | | INCREMENTAL | Deals Summary | Enabled by Default |
| [Filters Schema](https://developers.pipedrive.com/docs/api/v1/Filters#getFilters)        | | INCREMENTAL | Filters | Enabled by Default |
| [Pipelines Schema](https://developers.pipedrive.com/docs/api/v1/Pipelines)      | | INCREMENTAL | Pipelines | Enabled by Default |
| [Files Schema](https://developers.pipedrive.com/docs/api/v1/Files)          | | INCREMENTAL | Files | Enabled by Default |
| [Users Schema](https://developers.pipedrive.com/docs/api/v1/Users#getUsers)          | | INCREMENTAL | Users | Enabled by Default |
