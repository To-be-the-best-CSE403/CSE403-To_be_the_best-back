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
* This README.md file
* The `.github/workflows/` directory contains the files needed for GitHub Actions and its continuous integration features.
* The `.vscode/` directory contains the settings for a Visual Code Studio set up.
* The `backend/` directory which will contain the code used to handle and pass data from the database to the frontend.
* The `database/` directory which will contain the code to scrape information from websites and handle scraped information that will be stored in the database.

## Installation

- **Step 1**: Install `ToBeTheBest` Extension
  - **Firefox**: [Latest Release on Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/tobethebest/).
  - **Chrome**: [Latest Release on Github](https://github.com/To-be-the-best-CSE403/CSE403-To_be_the_best-front/releases/).
    - Download `tobethebest-chrome.zip` and unzip the file.
    - Go to `chrome://extensions/` and enable "Developer mode" in the top right corner.
    - Click `Load unpacked` and select the unzipped folder.

- **Step 2**: Go to [Pokemon Showdown](https://play.pokemonshowdown.com/) and activate the extension. 
  - **Firefox**: Go to extension setting and choose `Always Allow on play.pokemonshowdown.com`.
  - **Chrome**: Go to extension setting and allow the extension for `play.pokemonshowdown.com`.

- **Step 3***: Hover on the `ToBeTheBest` toggle button on the right side of the screen to show the extension's sidebar. 

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
