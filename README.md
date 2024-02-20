# ToBeTheBest Website For Pokemon Showdown

[![Vercel Production Deployment](https://github.com/To-be-the-best-CSE403/CSE403-To_be_the_best-back/actions/workflows/production.yml/badge.svg)](https://github.com/To-be-the-best-CSE403/CSE403-To_be_the_best-back/actions/workflows/production.yml)

Welcome to the [Website](https://tobethebest.vercel.app) repository for the ToBeTheBest [Extension](https://github.com/To-be-the-best-CSE403/CSE403-To_be_the_best-front) designed for Pokémon Showdown. Our website serves as a crucial component of the ToBeTheBest project, providing essential functionalities such as data visualization and API support for the extension. This repository contains the code for the backend of the website, which is built using Python Flask and Next.js.

## Table of Contents

- [Goals](#goals)
- [Repository Layout](#repository-layout)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [For Developers](#for-developers)
  - [Developing Locally](#developing-locally)
  - [Building](#building)
  - [Deploying](#deploying)
- [Issues](#issues-feature-requests-and-contributions)
- [Contributing](#issues-feature-requests-and-contributions)
- [License](#license)

## Goals

The objective of this repository is to develop the backend components of the extension. The website's functionalities are divided into two main components:

1. Database: Utilize web scraping techniques to gather Pokémon information and battle data from various sources. This data is then used to populate the database utilized by the web extension.

2. API: Develop an API to facilitate communication between the database and the frontend of the application. This API will handle data calculations and serve information to the frontend for user interaction.

## Repository Layout

The layout of the repository is as follows:

<details>
<summary>backend</summary>

- **api**: API endpoints serving data to the frontend.
  - index.py: Entry point for the API.
  - views.py: Contains the API routes.
  - test_views.py: Contains mock API routes for testing.
- **src**: Next.js App source code.
  - **api**: API logic and calculations.
  - **app**: Frontend pages for the website.
  - **components**: Reusable components for the website.
  - **config**: Configuration files for the website.
  - **data**: Data collection and processing.
- **tests**: Tests for the backend.
</details>

<details>
<summary>database</summary>

- **webscraper.py**: Python script for web scraping data for the database.

</details>

<details>
<summary>.github</summary>

- **workflows**: GitHub Actions and continuous integration.
- **ISSUE_TEMPLATE**: Templates for creating issues.
</details>

## Requirements

- Python 3.9
- Node.js 18.x
- Vercel CLI

## Installation

You can clone this repository with the following command:

```bash
git clone https://github.com/To-be-the-best-CSE403/CSE403-To_be_the_best-back.git
```

The API is using Python Flask. Create a python environment of your choice and install the required packages with the following commands:

```bash
python3.9 -m venv .venv    # Create a virtual environment or use your own
source .venv/bin/activate  # Activate the virtual environment
pip install -r requirements.txt
```

The website code is located in the `backend` directory. Install the node modules with the following command:

```bash
cd backend
npm install
```

## For Developers

### Developing Locally

To run the website locally, you can use the following commands:

```bash
npm run dev
```

This will start the Flask server and the Next.js server. The Flask server will be running on `http://127.0.0.1:5328` and the Next.js server will be running on `http://localhost:3000`.

### Building

To build the website, you can use the following commands:

```bash
npm run build
```

This will build the Next.js website into the `backend/.next` directory.

### Deploying

We are using Vercel to deploy the website since we are using Next.js. You can deploy it with the hosting provider of your choice.

#### Vercel

Create an account on [Vercel](https://vercel.com/) and follow the instructions for [Deploying to Vercel](https://vercel.com/docs/deployments/overview).

You can deploy the website on Vercel with the following command:

```bash
vercel deploy
```

#### Other Hosting Providers

Next.js can automatically create a `standalone` folder that copies only the necessary files for a production deployment. To leverage this automatic copying you can enable it in your `next.config.js`:

```javascript
module.exports = {
  output: "standalone",
};
```

## Issues, feature requests and contributions

- If you come across a problem with the extension, please open an [issue](https://github.com/To-be-the-best-CSE403/CSE403-To_be_the_best-back/issues/new/choose) and choose the bug report template.
- If you have a feature request, please open an [issue](https://github.com/To-be-the-best-CSE403/CSE403-To_be_the_best-back/issues/new/choose) with the feature request template.
- Contributions are always welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
