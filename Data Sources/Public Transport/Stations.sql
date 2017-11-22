/****** Script for SelectTopNRows command from SSMS  ******/
ALTER TABLE [dbo].PT
ADD [GeoLocation] GEOGRAPHY
GO

UPDATE [dbo].PT
SET [GeoLocation] = geography::STPointFromText('POINT(' + CAST([Lon] AS NVARCHAR) + ' ' + 
                    CAST([Lat] AS NVARCHAR) + ')', 4326)
GO

select count(*) from pt where ltrim(rtrim(Lon)) != ''

select top 5000 * from pt order by lon

pointA.Stdistance(pointB)

ALTER TABLE [dbo].City
ADD [GeoLocation] GEOGRAPHY
GO

UPDATE [dbo].City
SET [GeoLocation] = geography::STPointFromText('POINT(' + CAST([Longitude] AS NVARCHAR) + ' ' + 
                    CAST([Latitude] AS NVARCHAR) + ')', 4326)
GO

ALTER TABLE [dbo].City
ADD City_id int identity(1,1)
GO

SELECT p.[CommonName]
      ,p.[Lon]
      ,p.[Lat]
      ,p.[Identifier]
      ,p.[Direction]
      ,p.[Street]
      ,p.[Landmark]
      ,p.[Town]
      ,p.[Suburb]
      ,c.[City]
      ,c.[Area (sq km)]
      ,c.[Radius (km)]
      ,c.[Longitude]
      ,c.[Latitude]
      ,c.[Population]
      ,c.[City_id]
      ,c.Geolocation.STDistance(p.pGeolocation) as Distance 
into dbo.CrossJoin
  FROM [Uber].[dbo].[PT] p
  cross join dbo.city c

select
    * 
into dbo.City23
from dbo.crossjoin
where city_id = 23 and distance < (cast(([radius (km)]) as float) * 1000)

select * from dbo.crossjoin where distance < 500



select * from dbo.crossjoin2 where city_id = 7 and distance < 1000000


select * into dbo.all_cities from(
select * from city1
union all
select * from city2
union all
select * from city3
union all
select * from city4
union all
select * from city5
union all
select * from city6
union all
select * from city7
union all
select * from city8
union all
select * from city9
union all
select * from city10
union all
select * from city11
union all
select * from city12
union all
select * from city13
union all
select * from city14
union all
select * from city15
union all
select * from city16
union all
select * from city17
union all
select * from city18
union all
select * from city19
union all
select * from city20
union all
select * from city21
union all
select * from city22
union all
select * from city23
)a

select * from crossjoin where city = 'Bangor' and distance < 500


with cte as
(
SELECT distinct
    City
    ,count(Lon) over (partition by (city)) as Stations
    ,population
from [dbo].[all_cities]
group by city, lon, [population]
)

select 
    City
    ,cast([population]/stations as float) People_to_station
into People_to_station
from cte
order by People_to_station
