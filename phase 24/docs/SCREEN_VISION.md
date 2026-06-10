# Screen Vision

## Commands

```text
screen shot
screen ocr
image ocr C:\path\image.png
screen safety
desktop action open notepad
```

## Notes

- Screenshots save to `workspace/screens/`
- OCR requires Tesseract
- Desktop control is disabled by default:
  ```env
  SCREEN_CONTROL_ENABLED=false
  ```
