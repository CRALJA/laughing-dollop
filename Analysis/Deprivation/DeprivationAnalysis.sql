
/****** This calculates the average deprivation for each city by taking an average of the LSOA codes that belong to each city ******/
/****** The data for this can be found in Data Sources\Deprivation\Reduced_deprivation_file.csv ******/
SELECT DISTINCT
       [Local Authority District name (2013)],
       AVG(CAST([Index of Multiple Deprivation (IMD) Score] AS FLOAT)) OVER(PARTITION BY [Local Authority District name (2013)])
FROM [Uber].[dbo].[Deprivation2]
WHERE [Local Authority District name (2013)] IN('Bangor', 'Bath and North East Somerset', 'Birmingham', 'Bradford', 'Brighton and Hove', 'Bristol, City of', 'Cambridge', 'Canterbury', 'Cardiff', 'Carlisle', 'Chelmsford', 'Cheshire West and Chester', 'Chichester', 'Coventry', 'Derby', 'County Durham', 'East Cambridgeshire', 'Exeter', 'Gloucester', 'Herefordshire, County of', 'Kingston upon Hull, City of', 'Lancaster', 'Leeds', 'Leicester', 'Lichfield', 'Lincoln', 'Liverpool', 'London', 'Manchester', 'Newcastle upon Tyne', 'Newport', 'Norwich', 'Nottingham', 'Oxford', 'Peterborough', 'Plymouth', 'Portsmouth', 'Preston', 'St Albans', 'St Asaph', 'Salford', 'St David''s', 'Salisbury', 'Sheffield', 'Southampton', 'Stoke-on-Trent', 'Sunderland', 'Swansea', 'Truro', 'Wakefield', 'Wells', 'Winchester', 'Wolverhampton', 'Worcester', 'York')
GROUP BY [Local Authority District name (2013)],
         [Index of Multiple Deprivation (IMD) Score];