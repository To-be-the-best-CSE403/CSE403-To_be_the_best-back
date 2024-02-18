# ToBeTheBest Backend Repository

## Table of Contents

- [Project Overview](#project-overview)
- [Goals](#goals)
- [Repository Layout](#repository-layout)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

To Be the Best is a web browser extension that is used for Pokémon Showdown, an online Pokémon battle simulator,
to help users build teams and find movesets as well as provide recommendations for moves to use in battle.
This feature will help those who are new to Pokémon Showdown learn the mechanics of the game in addition to helping
those who are more experienced develop their skills, whether they are a casual or competitive player.

## Goals

The goals of the backend configuration of To Be the Best is to:

1. Scrap Pokémon information and Pokémon battle information from websites to populate the database used in the web extension
2. Send information and data calculations from the database and backend to the frontend of the application

## Repository Layout

The layout of the repository is as follows:

- This README.md file
- The `.github/workflows/` directory contains the files needed for GitHub Actions and its continuous integration features.
- The `.vscode/` directory contains the settings for a Visual Code Studio set up.
- The `backend/` directory which will contain the code used to handle and pass data from the database to the frontend.
- The `database/` directory which will contain the code to scrape information from websites and handle scraped information that will be stored in the database.

## Website

### Requirements

- Python 3.9
- Node.js 18.x
- Vercel CLI

### Installation

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

## Extension

GitHub: [ToBeTheBest Extension](https://github.com/To-be-the-best-CSE403/CSE403-To_be_the_best-front)

### Installation

- **Step 1**: Install `ToBeTheBest` Extension

  - **Firefox**: [Latest Release on Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/tobethebest/).
  - **Chrome**: [Latest Release on Github](https://github.com/To-be-the-best-CSE403/CSE403-To_be_the_best-front/releases/).
    - Download `tobethebest-chrome.zip` and unzip the file.
    - Go to `chrome://extensions/` and enable "Developer mode" in the top right corner.
    - Click `Load unpacked` and select the unzipped folder.

- **Step 2**: Go to [Pokemon Showdown](https://play.pokemonshowdown.com/) and activate the extension.

  - **Firefox**: Go to extension setting and choose `Always Allow on play.pokemonshowdown.com`.
  - **Chrome**: Go to extension setting and allow the extension for `play.pokemonshowdown.com`.

## Usage

The purpose of this repository is to serve as a guide for how data is stored and communicated between the database and the frontend of the extension.
The user is not intended to manipulate the code in this repository.

## Contributing

If you would like to contribute to this project, please contact one of the owners. Any help would be appreciated!

## License

MIT License

Copyright (c) [2024] [To Be The Best]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

```
