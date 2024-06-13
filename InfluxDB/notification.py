from telepyth import TelepythClient

tp = TelepythClient()
tp.send_text('Hello, World!')  # notify with plain text
tp.send_text('_bold text_ and then *italic*')  # or with markdown formatted text