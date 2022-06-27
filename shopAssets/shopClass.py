import discord, os, importlib, sys

class Shop:
    items = {}

    def loadItems(self):
        for file in os.listdir("shopAssets\items"):
            if not file.endswith(".py"):
                continue
            name = "shopAssets.items."+file.removesuffix(".py")
            name = importlib.util.resolve_name(name, None)
            spec = importlib.util.find_spec(name)
            lib = importlib.util.module_from_spec(spec)
            sys.modules[name] = lib
            spec.loader.exec_module(lib)
            setup = getattr(lib, "setup")
            setup(self)

            print(f"{name.split('.')[-1]} ShopItem successfully loaded.")

    async def initShop(self, ctx):
        class DropList(discord.ui.View):
            items = self.items

            @discord.ui.select(placeholder="Выберите предмет для покупки...", min_values=1, max_values=1, options=[
                discord.SelectOption(
                    label=item.name,
                    description=item.description
                ) for item in self.items.values()
            ])
            async def callback(self, select, interaction: discord.Interaction):
                await self.items[select.values[0]].sendEmbed(interaction, member=interaction.user, ctx=ctx)

        return DropList()