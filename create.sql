CREATE TABLE all_weeks_countries
(
  country_name VARCHAR(255) NOT NULL,
  country_iso2 VARCHAR(2) NOT NULL,
  week VARCHAR(255) NOT NULL,
  category INT NOT NULL,
  weekly_rank VARCHAR(255) NOT NULL,
  show_title VARCHAR(255) NOT NULL,
  season_title VARCHAR(255) NOT NULL,
  cumulative_weeks_in_top_10 VARCHAR(255) NOT NULL,
  PRIMARY KEY (show_title)
);

CREATE TABLE all_weeks_global
(
  week INT NOT NULL,
  category VARCHAR(255) NOT NULL,
  weekly_rank INT NOT NULL,
  show_title VARCHAR(255) NOT NULL,
  season_title VARCHAR(255) NOT NULL,
  cumulative_weeks_in_top_10 VARCHAR(255) NOT NULL,
  PRIMARY KEY (show_title),
  FOREIGN KEY (country_name) REFERENCES all_weeks_countries(show_title)
);

CREATE TABLE most_popular
(
  category VARCHAR(255) NOT NULL,
  rank VARCHAR(255) NOT NULL,
  show_title VARCHAR(255) NOT NULL,
  season_title VARCHAR(255) NOT NULL,
  hours_viewed_first_28_days INT NOT NULL,
  PRIMARY KEY (show_title),
  FOREIGN KEY (country_name) REFERENCES all_weeks_countries(show_title)
);
