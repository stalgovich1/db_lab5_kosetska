DO $$ 
DECLARE
    counter INT := 1;
BEGIN
    -- Починаємо цикл
    LOOP
        -- Вставка тестових даних в таблицю MoviesAndShows
        INSERT INTO MoviesAndShows (MovieOrShowID, Title, Type, ReleaseYear)
        VALUES (counter + 1000, 'Фільм/шоу ' || counter, 'Тип ' || counter, 2000 + counter);

        -- Вставка тестових даних в таблицю Weeks
        INSERT INTO Weeks (WeekID, WeekStartDate, WeekEndDate)
        VALUES (counter + 1000, CURRENT_DATE + counter, CURRENT_DATE + counter + 6);

        -- Вставка тестових даних в таблицю Countries
        INSERT INTO Countries (CountryID, CountryName)
        VALUES (counter + 1000, 'Країна ' || counter);

        -- Вставка тестових даних в таблицю Ratings
        INSERT INTO Ratings (RatingID, MovieOrShowID, WeekID, CountryID, Rank, Viewership, Duration)
        VALUES (counter + 1000, counter + 1000, counter + 1000, counter + 1000, counter, 100000 + counter * 10000, 120 + counter);

        -- Збільшуємо лічильник
        counter := counter + 1;

        -- Перевіряємо, чи потрібно завершити цикл
        EXIT WHEN counter > 10; -- Замініть 10 на кількість рядків, яку ви хочете вставити
    END LOOP;
END $$;
