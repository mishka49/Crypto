from coins.models import Coin


class CoinRepository:
    @staticmethod
    def create_or_update(coin):
        fields = Coin._meta.fields
        Coin.objects.update_or_create(
            id=coin['id'],
            defaults={field.name: coin[field.name] for field in fields}
        )


if __name__=="__main__":
    CoinRepository.create_or_update("some")
