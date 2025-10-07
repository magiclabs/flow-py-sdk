from examples.common import Config
from examples.common import Example
from magic_flow import flow_client


class CreateClientExample(Example):
    """
    Use the client to get an accounts deployed contracts
    """

    def __init__(self) -> None:
        super().__init__(tag="C.1.", name="Get Account Contracts", sort_order=51)

    async def run(self, ctx: Config):
        async with flow_client(host=ctx.access_node_host, port=ctx.access_node_port) as client:
            script = await client.get_account_at_latest_block(
                address=ctx.service_account_address.bytes
            )

            self.log.info(f"Account contracts length {len(script.contracts)}")
