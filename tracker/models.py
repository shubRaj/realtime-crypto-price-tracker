from django.db import models

class Crypto(models.Model):
    """
    Model representing a cryptocurrency.
    """
    name = models.CharField(
        max_length=50, 
        unique=True, 
        verbose_name="Crypto Name"
    )
    symbol = models.CharField(
        max_length=30, 
        unique=True, 
        verbose_name="Symbol"
    )

    def __str__(self) -> str:
        """
        String representation of the Crypto model.
        
        Returns:
            str: The symbol of the cryptocurrency.
        """
        return self.symbol

    def __repr__(self) -> str:
        """
        Official string representation of the Crypto model.
        
        Returns:
            str: The official string representation, using the __str__ method.
        """
        return super().__str__()

class Price(models.Model):
    """
    Model representing the price of a cryptocurrency.
    """
    price = models.DecimalField(
        max_digits=30, 
        decimal_places=4
    )
    symbol = models.ForeignKey(
        Crypto, 
        on_delete=models.CASCADE, 
        related_name="prices", 
        related_query_name="price"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        """
        Meta class for the Price model to define ordering and latest retrieval.
        """
        ordering = ("created_at",)
        get_latest_by = "created_at"

    def __str__(self) -> str:
        """
        String representation of the Price model.
        
        Returns:
            str: The name of the cryptocurrency symbol associated with the price.
        """
        return self.symbol.name

    def __repr__(self) -> str:
        """
        Official string representation of the Price model.
        
        Returns:
            str: The official string representation, using the __str__ method.
        """
        return super().__str__()
