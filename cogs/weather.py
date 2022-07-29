import disnake
from disnake.ext import commands
import requests
import os


class WeatherCommand(commands.Cog):
    @commands.slash_command(name = "погода", description="Информация о погоде")
    async def weather(self, inter: disnake.ApplicationCommandInteraction, city: str):
        weathertoken = open('weathertoken.txt', 'r').readline()
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = city
        city_name_cap = city_name.capitalize()
        complete_url = base_url + "appid=" + weathertoken + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        channel = inter.response.send_message

        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_pressure = current_pressure * 7.50062*(10**-3) * 100
            current_pressure = int(current_pressure)
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]

            embed = disnake.Embed(title=f"Погода в городе {city_name_cap}",
                                    color=inter.guild.me.top_role.color,)
            embed.add_field(name="Описание", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Температура(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
            embed.add_field(name="Влажность(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Атмосферное давление", value=f"**{current_pressure} мм рт. ст.**", inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text=f"Запрос от {inter.author.name}")
            await inter.send(embed=embed)
        else:
            await inter.response.defer()
            await inter.edit_original_message("Город не найден")


def setup(bot: commands.Bot):
    bot.add_cog(WeatherCommand(bot))
    print(f"> Extension {__name__} is ready")