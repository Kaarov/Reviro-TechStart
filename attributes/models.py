from django.db import models
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile

from users.models import User, Partner


class Beverage(models.Model):
    name = models.CharField("Name", max_length=255)
    category = models.CharField("Category", max_length=255)
    price = models.PositiveIntegerField("Price", default=0)
    description = models.TextField("Description", null=True, blank=True)
    availability_status = models.BooleanField("Availability Status", default=True)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='beverage_partner')

    class Meta:
        verbose_name = "Beverage"
        verbose_name_plural = "Beverages"

    def __str__(self):
        return self.name


class Subscription(models.Model):
    class Subscriptions(models.TextChoices):
        month_1 = "1-month"
        month_3 = "3-month"
        month_6 = "6-month"
        year = "1-year"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription_user')
    duration = models.CharField("Subscription", max_length=10, choices=Subscriptions.choices, null=True, blank=True)
    start_date = models.DateField("Start Date", auto_now_add=True)
    end_date = models.DateField("End Date", auto_now_add=True)
    status = models.BooleanField("Status", default=True)

    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"

    def __str__(self):
        return f'{self.user.username} - {self.duration}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_user')
    establishment = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='establishment_partner')
    beverage = models.ForeignKey(Beverage, on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField("Order Date", auto_now_add=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f'{self.user.username} - {self.establishment}'


class QRCode(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='qrcode_partner')
    qrcode = models.ImageField("QR Code Image", upload_to='qrcodes/', blank=True, null=True)
    beverage_menu = models.ForeignKey(Beverage, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(f"Partner: {self.partner.user.username}")
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Save QR code image to model
        img_byte_array = BytesIO()
        img.save(img_byte_array, format='PNG')
        img_content = ContentFile(img_byte_array.getvalue())
        self.qrcode.save(f'qrcode_{self.partner.user.username}.png', img_content, save=False)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "QRCode"
        verbose_name_plural = "QRCodes"

    def __str__(self):
        return self.partner.user.username