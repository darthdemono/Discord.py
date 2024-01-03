import requests
import json
import discord
from discord.ext import commands, tasks
from discord.utils import get
import csv

get = "GET"


class Covid(commands.Cog):
    """
    Covid-19 News
    """

    def __init__(self, client):
        self.client = client

    @commands.command(
        aliases=["Covid-19", "corona", "covid-19"],
        help="Gives Covid Info"
    )
    async def covid(self, ctx, arg):
        try:
            url = "https://covid-193.p.rapidapi.com/statistics"
            Country = f"{arg}"
            params = {"country": f"{Country}"}
            headers = {
                "x-rapidapi-key": "10f6f92058msh0cb2834f5fa8f67p174564jsn52f240dfbf79",
                "x-rapidapi-host": "covid-193.p.rapidapi.com"
            }
            response = requests.request(
                get, url, headers=headers, params=params)
            data = response.text
            dic = {}
            with open("csv/wikipedia-iso-country-codes.csv") as f:
                file = csv.DictReader(f, delimiter=',')
                for line in file:
                    dic[line['English short name lower case']
                        ] = line['Alpha-2 code']
            CountryName = [Country]
            for country in CountryName:
                CountryCode = dic[country].lower()
            Country = json.loads(data)["response"][0]["country"]
            Population = json.loads(data)["response"][0]["population"]
            New_Cases = json.loads(data)["response"][0]["cases"]["new"]
            Total_Cases = json.loads(data)["response"][0]["cases"]["total"]
            Recovered_Cases = json.loads(
                data)["response"][0]["cases"]["recovered"]
            Active_Cases = json.loads(data)["response"][0]["cases"]["active"]
            Total_Deaths = json.loads(data)["response"][0]["deaths"]["total"]
            New_Deaths = json.loads(data)["response"][0]["deaths"]["new"]
            Total_Tests = json.loads(data)["response"][0]["tests"]["total"]
            Date = json.loads(data)["response"][0]["day"]
            embed = discord.Embed()
            embed.title = f"Covid info of {Country}"
            embed.set_thumbnail(
                url=f"https://flagcdn.com/256x192/{CountryCode}.png")
            embed.add_field(
                name="Population",
                value=f"{Population}",
                inline=True
            )
            embed.add_field(
                name="New Cases",
                value=f"{New_Cases}",
                inline=True
            )
            embed.add_field(
                name="Total Cases",
                value=f"{Total_Cases}",
                inline=True
            )
            embed.add_field(
                name="Recovered Cases",
                value=f"{Recovered_Cases}",
                inline=True
            )
            embed.add_field(
                name="Active Cases",
                value=f"{Active_Cases}",
                inline=True
            )
            embed.add_field(
                name="Total Deaths",
                value=f"{Total_Deaths}",
                inline=True
            )
            embed.add_field(
                name="New Deaths",
                value=f"{New_Deaths}",
                inline=True
            )
            embed.add_field(
                name="Total Deaths",
                value=f"{Total_Deaths}",
                inline=True
            )
            embed.add_field(
                name="Date",
                value=f"{Date}",
                inline=True
            )
            await ctx.send(
                embed=embed
            )
        except Exception as err:
            await ctx.channel.send(f"❌Counldn't Send Stats {err}")

    @covid.error
    async def covid_handler(self, ctx, error):
        if isinstance(error, commands.error.MissingRequiredArgument):
            await ctx.channel.send(f"❌ **Give the name of a Country {error}**")


def setup(client):
    client.add_cog(Covid(client))
