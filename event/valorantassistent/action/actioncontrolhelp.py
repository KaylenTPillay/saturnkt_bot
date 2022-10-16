class ActionControllerHelp:

    async def handle_action(self, context, args):
        await context.send("Use `$HeyCypher` [command] [optional info]")
