from discord.ext import commands
import discord
import random
import time


# noinspection PyUnusedLocal
class General(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket and API latency."""

        start_time = time.time()
        message = await ctx.send("Testing ping...")
        end_time = time.time()

        await message.edit(content=f"Pong! `Websocket: {round(self.bot.latency * 1000, 2)}ms`, "
                                   f"`API: {round((end_time - start_time) * 1000, 2)}ms`")

    @commands.command(name="setstatus")
    @commands.cooldown(rate=1, per=30)
    async def setstatus(self, ctx: commands.Context, *, text: str):
        """Set the bot's status."""
        # TODO: unsetting status
        await self.bot.change_presence(activity=discord.Game(name=text))

    @setstatus.error
    async def setstatus_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"This command is on cooldown, try again after {round(error.retry_after)} seconds.",
                           delete_after=5)
        print(error)

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
