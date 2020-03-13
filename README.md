# JSON API Docs

## 1.  Sending simple message
```
{
  "entries":[
    {
      "template_type":"message",
      "message":"Hi, greetings from Makerobos", // type:string , max-length:450
      "full_width" : false, // type:boolean | set the width of message card to full width of the chat screen if true
      "text_color" : '#fff', // type:string, valid css color code to apply as font color for the message
      "background_color":  '#000', // type:string, valid css color code to apply as background color for the message
      "script": 'console.log("hello")', // type:string, any valid js script to run with this card
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
        "buttons":[ // maximum 3 buttons
          {
            "type":"url",
            "url":"https://www.makerobos.com",
            "webview_height":"full", // "full" | "small" | "medium" | "new" (opens in new tab)
            "title":"Preview"
          },
          {
            "type":"url",
            "url":"https://www.makerobos.com",
            "webview_height":"small",
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
      "slides":[ // maximum 9 slides
          {
            "title":"some title",
            "subtitle":"some description",
            "image_url":"https://someimage.jpg",
            "shadow": false, // type: boolean, adds an shadow overlay on the image for visiblity of text
            "preview": 'landscape', // type: string, default: landscape, values: (landscape | square), set the ratio of images to display in carousal card
            "card_style": 'carousel' // type: string, values : (carousel | slideshow | infocard), default: carousel
            "buttons":[ // maximum three buttons
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
            "image_url":"https://www.images.com/someimage.jpg"
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
      "template_type":"video", // “image” | “audio” | “video”
      "url":"https://www.youtube.com/watch?v=-JLewvWBkCw",
      "full_width": false, // type: boolean, 
      "background_color": "#fff",
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

## 6.  Button Types
```
{
  "buttons":[
    {
      "type":"url",
      "url":"https://www.makerobos.com",
      "webview_height":"small", // "full" | "small" | "medium" | "new" (opens in new tab)
      "title":"Preview"
    },
    {
      "type":"go_to",
      "next_block":"welcome", // A valid block name in your bot
      "title":"Preview"
    },
    {
      "type":"whatsapp",
      "text":"Hi i'am Bot", // message text
      "mobile": "+915656526526" // number to send the message
      "title":"Preview"
    },
    {
      "type":"messenger",
      "messenger_id":"<messenget_id>",      
      "title":"Preview"
    },
    {
      "type":"phone",
      "phone_number":"+919999999999",      
      "title":"Preview"
    }
  ]
}
```

## 7. Go To blocks
```
{
  "entries":[
    {
      "template_type":"go_to",
      "go_to_blocks": ["welcome", "default", "someblock"], // type: list of strings, valid list of block names in that bot
      "execution_type": "sequentially", // type: string, default: sequentially , values: (sequentially | randomly), if sequentially is set all bocks in the list will be executed, else randomly only one block will run 
    }
  ]
}
```


## 8. Autosuggest using Webhook

### 8.1 key value pair list format
``` 
[
    {"__display":"India", "code":"+91" },
    {"__display":"US", "code":"+1" },
    {"__display":"China", "code":"+86" }
]
 ```
### 8.2 new line seperated list
```
India
US
China
```
