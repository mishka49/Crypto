from coins.models import Coin


class CoinRepository:
    @staticmethod
    def create_or_update(coin):
        print("COIN::", coin.name)
        fields = Coin._meta.fields
        values = [value for _, value in coin.__dict__.items() if _ in [field.name for field in fields]]
        Coin.objects.update_or_create(
            id=coin.id,
            defaults={field.name: value for field, value in zip(fields, values)}
        )


if __name__ == "__main__":
    CoinRepository.create_or_update("some")
