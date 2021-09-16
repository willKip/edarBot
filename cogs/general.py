from discord.ext import commands
import random


class General(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket latency."""
        await ctx.send(f"Pong! Responded in `{round(self.bot.latency * 1000, 2)}ms`")

    @commands.command()
    async def roll(self, ctx, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split("d"))
        except (ValueError, Exception):
            await ctx.send("Format has to be in NdN!")
            return

        result = ", ".join(str(random.randint(1, limit)) for _ in range(rolls))
        await ctx.send(result)

    @commands.command(description="For when you wanna settle the score some other way")
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))


def setup(bot: commands.Bot):
    bot.add_cog(General(bot))
