from enum import Enum
from event.valorantassistent.action.actioncontrolhelp import ActionControllerHelp

class EventControllerValorantAssistent:

    async def handle_event(self, context, args):
        action_type = self.__get_action_from_args(args)
        action_data_args = self.__get_action_data_args(args)

        await self.__process_event(context, action_type, action_data_args)

    def __get_action_from_args(self, args):
        if len(args) == 0:
            return _ActionType.UNKNOWN

        action_type = _ActionType.UNKNOWN
        try:
            action_value = args[0].lower()
            action_type = _ActionType(action_value)
        except ValueError as err:
            action_type = _ActionType.UNKNOWN

        return action_type

    def __get_action_data_args(self, args):
        action_data_args = []
        event_args_len = len(args)
        if (event_args_len > 1):
            action_data_args = args[1:]

        return action_data_args

    async def __process_event(self, context, type, args):
        if type == _ActionType.HELP:
            controller = ActionControllerHelp()
            await controller.handle_action(context, args)
        elif type == _ActionType.UNKNOWN:
            await context.send("I don't support that command")

class _ActionType(Enum):
    UNKNOWN = ''
    HELP = 'help'
