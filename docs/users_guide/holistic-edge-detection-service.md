![SingularityNet.io](../images/singnet-logo.jpg?raw=true 'SingularityNET')

[![CircleCI](https://circleci.com/gh/IsraelAbebe/pytorch-hed.svg?style=svg)](https://circleci.com/gh/IsraelAbebe/pytorch-hed)

# Holistically-Nested Edge Detection


## Welcome

This service provides edge detection service for given images using pytorch frameworks based on the paper [Holistically-Nested Edge Detection](https://arxiv.org/abs/1504.06375).

The main difference from Canny edge detection is that this approch provides better edge detection for training 
since it picks up useful edges rather than providing all edges that exist and it reduces noice in that way.

## How does it work?
- The user would provide base64 encoded in utf-8 format of image file.
- The historical artifact of image_type would be removed in the next major upgrade.
- This image after being accepted would be then be converted to 480 * 320 like `cv2.resize(x, (480,320))`
- The Holistic Edge Detector would do it job and provide us with an image that has is representation of the edges.
- Image then will be converted to image using 'base64.b64decode'.

# Using the service on the platform
The returned result has the following form:

```proto
message ImageFile {
	string image = 1;
	string image_type = 2;
}
```

As mentioned above the input image is `utf-8` encoded base64 string. The image_type is automatically infered from numpy 
arrays currently.

The result is 480x320 image currently with the format given above.

A simple conversion script that handles the result is: 
```python
result_image = self.client.send_request(stub, self.image, self.image_type)
binary_image = base64.b64decode(result_image)
# As said, we can use magic to infer the file type for the given string by infering stream.
file_format = magic.from_buffer(binary_image, mime=True).split('/')[1]

with open("images/client_out2." + file_format, 'wb') as f:
    f.write(binary_image)
```
     
Example result after saving the image might look like

![Expected output](../images/client_out.png?raw=true 'SingularityNET')
