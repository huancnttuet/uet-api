# Send to single device.
from pyfcm import FCMNotification
from . import device
API_KEY = "AAAAXsPpUNE:APA91bGeXH6azmaVcJuOAgoz4c5BMJV6vk3mx0ZAgrEEcM71-KG7T996vOhJKDLIwrdxIEbvFSRqMLJ0HXQM8aCA03HghraviJrkTbb4Kr1R7CK8ODvc-l8N2va7IqLIieD2FX62YjQU"


def send_notify(title, message):
    push_service = FCMNotification(api_key=API_KEY)

    # OR initialize with proxies

    # proxy_dict = {
    #           "http"  : "http://127.0.0.1",
    #           "https" : "http://127.0.0.1",
    #         }
    # push_service = FCMNotification(api_key="<api-key>", proxy_dict=proxy_dict)

    # Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

    # registration_id = "dHgoSI8XRc-b4oqhGiOHgu:APA91bEQVjg-ZEYOyT2LqGZGkwuE4mQStwk7wSMBWJPpqxIterzzftnleW7SQuCRspdfoIxT1E2zGcExJettfZXj9K5dtHWj8gCop3A8yfwY1XoACXmvMqhKNVV704YtEgkt345W8xNp"

    # result = push_service.notify_single_device(registration_id=registration_id,
    #                                            message_title=title,
    #                                            message_body=message)

    # Send to multiple devices by passing a list of ids.

    registration_ids = device.get_all_device_id()

    # Sending a notification with data message payload
    data_message = {
        "Nick" : "Mario",
        "body" : "great match!",
        "Room" : "PortugalVSDenmark"
    }
    # To multiple devices
    result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_body=message, data_message=data_message)

    print(result)
   
