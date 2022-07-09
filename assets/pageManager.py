import discord


class PageManager:
    page = 0


    def __init__(self, pages: list, member: discord.Member, embed=True):
        self.pages = pages
        self.embed = embed
        self.member = member


    async def sendEmbed(self, ctx):
        kwarg = {"embed" if self.embed else "content": self.pages[self.page]}
        manager = self

        class View(discord.ui.View):
            @discord.ui.button(label="Назад", style=discord.ButtonStyle.primary)
            async def backward(self, button, interaction):
                await interaction.response.defer()
                if interaction.user != manager.member or manager.page == 0:
                    return

                manager.page -= 1

                kwarg = {"embed" if manager.embed else "content": manager.pages[manager.page]}
                await interaction.message.edit(**kwarg)

            @discord.ui.button(label="Вперёд", style=discord.ButtonStyle.primary)
            async def forward(self, button, interaction):
                await interaction.response.defer()
                if interaction.user != manager.member or manager.page == len(manager.pages) - 1:
                    return

                manager.page += 1

                kwarg = {"embed" if manager.embed else "content": manager.pages[manager.page]}
                await interaction.message.edit(**kwarg)


        await ctx.reply(**kwarg, view=View())
