# JSON API Docs

## 1.  Sending simple message
```
{
  "entries":[
    {
      "Template_type":"message",
      "message":"click the below button to view the demo." // type:string , max-length:450
    }
  ]
}
```

## 2.  Sending messages with buttons

```
{
  "entries":[
      {
        "template_type":"message",
        "message":"click the below button to view the demo.",
        "Buttons":[ // maximum three buttons
          {
            "type":"url",
            "url":"https://www.makerobos.com",
            "webview_height":"new",
            "title":"Preview"
          },
          {
            "type":"url",
            "url":"https://www.makerobos.com",
            "webview_height":"new",
            "title":"Preview"
          }
        ]
    }
   ]
}
```

## 3.  Sending carousels
```
{
  "entries":[
    {
      "template_type":"carousel",
      "shadow":true,
      "Slides":[ // maximum 9 slides
          {
            "title":"some title",
            "subtitle":"some description",
            "image_url":"https://someimage.jpg",
            "Buttons":[ // maximum three buttons
                {
                  "type":"url",
                  "url":"https://www.makerobos.com",
                  "webview_height":"new",
                  "title":"Preview"
                },
                {
                  "type":"url",
                  "url":"https://www.makerobos.com",
                  "webview_height":"new",
                  "title":"Preview"
                }
              ]
          },
          {
            "title":"some title",
            "subtitle":"some description",
            "Image_url":"https://www.images.com/someimage.jpg"
          }
      ]
     }
    ]
}
```
## 4. Sending Images, Videos, Audios
```
{
  "entries":[
    {
      "Template_type":"video", // “image” | “audio” | “video”
      "url":"https://www.youtube.com/watch?v=-JLewvWBkCw",
      "button":{
        "type":"url",
        "url":"https://digital.makerobos.com",
        "webview_height":"small",
        "title":"Preview"
      }
    }
  ]
}
```

## 5.  Setting attribute
```
{
  "entries":[
    {
      "template_type":"set_attr",
      "attributes":[
        {
        "attribute":"first_name",
        "value":"John"
        },
        {
        "attribute":"subscribed_email",
        "value":"john@mail.com"
        }
      ]
    }
  ]
}
```
