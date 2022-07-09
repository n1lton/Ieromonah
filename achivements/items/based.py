from achivements.achivementClass import Achivement

based = Achivement(
    "Это база!",
    1,
    "БАЗА БАЗА БАЗА ОЧЕНЬ БАЗИРОВАННО ОЛДЖ",
    4
)

@based.setCheck
async def check(member):
    return True






def setup(manager):
    manager.addAchivement(based)