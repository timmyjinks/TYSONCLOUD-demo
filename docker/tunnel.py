import os

from cloudflare import Cloudflare
from dotenv import load_dotenv

load_dotenv()

cloudflare_token = os.getenv("CLOUDFLARE_API_TOKEN", "")
tunnel_id = os.getenv("TUNNEL_ID", "")
account_id = os.getenv("ACCOUNT_ID", "")
zone_id = os.getenv("ZONE_ID", "")


cf = Cloudflare(api_token=cloudflare_token)


def create_public_url(name):
    try:
        cf.dns.records.create(
            zone_id=zone_id,
            name=name,
            type="CNAME",
            content=f"{tunnel_id}.cfargotunnel.com",
            proxied=True,
        )

        tunnel = cf.zero_trust.tunnels.cloudflared.configurations.get(
            account_id=account_id,
            tunnel_id=tunnel_id,
        )

        if tunnel is None:
            return
        if tunnel.config is None:
            return
        if tunnel.config.ingress is None:
            return

        ingress = tunnel.config.ingress
        fallback = ingress.pop()

        ingress.append(
            {
                "hostname": f"{name}.tysonjenkins.dev",
                "service": f"tcp://{name}",
            }
        )
        ingress.append(fallback)

        data = {"config": {"ingress": ingress}}

        cf.zero_trust.tunnels.cloudflared.configurations.update(
            tunnel_id=tunnel_id, account_id=account_id, **data
        )

    except NameError:
        print(NameError)
