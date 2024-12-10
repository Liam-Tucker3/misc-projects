# misc-projects
Small, miscellaneous projects to learn technologies

## Future Ideas
- **Year Prediction App**: An application where users can log in and make predictions of upcoming events.
  - The simplest version is a static series of binary questions (i.e. there will be snow in Tuscaloosa in 2025, Alabama Men's Basketball will make the Final Four, Dune 2 will win Best Picture at the Oscars) whose final results are manually added when the time comes. There will be two basic scoring systems: one where a user gets one point for each correct guess and one where users get points for correct answers weighted by the proportion of the user base who chose correctly.
  - A more complicated version would allow for categorical or continuous questions too, with their own scoring systems.
  - A more complicated version allows users to create groups and see a leaderboard of their friends.
  - A more complicated version allows users to create their own questions (and manually set the result when the time comes)
- **NFL Prediction App**: An application built on 538's NFL Prediction Game (https://github.com/fivethirtyeight/nfl-elo-game).
  - The simplest version allows users to predict each team's odds of winning each manually-added game, on a spectrum from 0% to 100%. Scores are set using a Brier score such that, if a team has a X% chance of winning a game, you maximize your expected points by giving this team an X% chance of winning.
  - A slightly more complicated version expands on 538's Elo Score to give a baseline
  - A slightly more complicated version expands to include other prediction ratings
  - A slightly more complicated version uses web scraping or APIs to automate the process of logging games and scores
  - Once the framework is built, the app can easily be extended to other sports, each with the same challenges.
