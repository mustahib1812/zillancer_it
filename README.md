# Zillancer

This is a basic Django application intended to provide a understanding of my Coding abilities

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)

## Usage

I have created this assignment to solve the below exercises.

  1- Create a GET api for CRMLed model in crm application

  2- Create a GET api for MASSlm model in master application.

  3- Create an API to get forecast amount from Opportunity model.

  I have added all the necessary comments in the Code itself for better understanding of what was the issue and how did I fix it. I hope it provides a better clarity

### Prerequisites

List any prerequisites that users need to have installed before they can use your project. For example:

- Python 3.2.12
- Django 3.2.12

### Installation

All other package dependencies are needed to be installed from requirements.txt file using command below:

Install the package dependencies:

  ```bash
   pip install -r <location-of-requirements.txt file>
  ```

## API Reference

#### Get CRM LED

```http
  GET /crm/v1/fetch-crm-led
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `crm_id` | `integer` | **Optional**. Id of crm to fetch|


#### Get CRM LED

```http
  GET /master/v1/fetch-masslm
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `integer` | **Optional**. Id of item to fetch|




#### Get Forecase Amount

```http
  GET /crm/v1/fetch-forecast-amount
```


