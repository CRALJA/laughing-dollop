
/****** This works out the number of people which one station serves (on average), in the cities that Uber does not serve ******/

ALTER TABLE [dbo].PT --PT means public transport
ADD [GeoLocation] GEOGRAPHY;
GO
UPDATE [dbo].PT
  SET
      [GeoLocation] = geography::STPointFromText('POINT('+CAST([Lon] AS NVARCHAR)+' '+CAST([Lat] AS NVARCHAR)+')', 4326);  --Create a new column which is the longitude and latitude of each station in a format which SQL understands
GO
ALTER TABLE [dbo].City
ADD [GeoLocation] GEOGRAPHY;
GO
UPDATE [dbo].City
  SET
      [GeoLocation] = geography::STPointFromText('POINT('+CAST([Longitude] AS NVARCHAR)+' '+CAST([Latitude] AS NVARCHAR)+')', 4326);
GO
ALTER TABLE [dbo].City
ADD City_id INT IDENTITY(1, 1);
GO
SELECT p.[CommonName],
       p.[Lon],
       p.[Lat],
       p.[Identifier],
       p.[Direction],
       p.[Street],
       p.[Landmark],
       p.[Town],
       p.[Suburb],
       c.[City],
       c.[Area (sq km)],
       c.[Radius (km)],
       c.[Longitude],
       c.[Latitude],
       c.[Population],
       c.[City_id],
       c.Geolocation.STDistance(p.pGeolocation) AS Distance
INTO dbo.CrossJoin
FROM [Uber].[dbo].[PT] p
     CROSS JOIN dbo.city c;  --Do a cross join from which I filter out the relevant results later

SELECT *
INTO dbo.City23
FROM dbo.crossjoin
WHERE city_id = 23
      AND distance < (CAST(([radius (km)]) AS FLOAT) * 1000);  -- for each non-Uber city, I put the nearby stations into a seperate table 

--Union the tables of each city into one

SELECT *
INTO dbo.all_cities
FROM
(
    SELECT *
    FROM city1
    UNION ALL
    SELECT *
    FROM city2
    UNION ALL
    SELECT *
    FROM city3
    UNION ALL
    SELECT *
    FROM city4
    UNION ALL
    SELECT *
    FROM city5
    UNION ALL
    SELECT *
    FROM city6
    UNION ALL
    SELECT *
    FROM city7
    UNION ALL
    SELECT *
    FROM city8
    UNION ALL
    SELECT *
    FROM city9
    UNION ALL
    SELECT *
    FROM city10
    UNION ALL
    SELECT *
    FROM city11
    UNION ALL
    SELECT *
    FROM city12
    UNION ALL
    SELECT *
    FROM city13
    UNION ALL
    SELECT *
    FROM city14
    UNION ALL
    SELECT *
    FROM city15
    UNION ALL
    SELECT *
    FROM city16
    UNION ALL
    SELECT *
    FROM city17
    UNION ALL
    SELECT *
    FROM city18
    UNION ALL
    SELECT *
    FROM city19
    UNION ALL
    SELECT *
    FROM city20
    UNION ALL
    SELECT *
    FROM city21
    UNION ALL
    SELECT *
    FROM city22
    UNION ALL
    SELECT *
    FROM city23
) a;
GO
WITH cte
     AS (
     SELECT DISTINCT
            City,
            COUNT(Lon) OVER(PARTITION BY(city)) AS Stations,
            population
     FROM [dbo].[all_cities]
     GROUP BY city,
              lon,
              [population])
     SELECT City,
            CAST([population] / stations AS FLOAT) People_to_station
     --INTO People_to_station
     FROM cte
     ORDER BY People_to_station;
