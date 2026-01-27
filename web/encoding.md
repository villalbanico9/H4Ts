---
hidden: true
layout:
  width: wide
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
---

# Encodings

### Encode

{% tabs %}
{% tab title="URL" %}
```bash
echo -n "<content>" | jq -sRr @uri
```
{% endtab %}

{% tab title="Base64" %}
```bash
echo -n "<content>" | base64 -w 0
```
{% endtab %}

{% tab title="Hex" %}
```bash
echo -n "<content>" | xxd -p -c 0
```
{% endtab %}

{% tab title="Decimal" %}
```bash
echo -n "<content>" | od -An -tuC | tr -s '\n' ' '
```
{% endtab %}
{% endtabs %}

### Decode

{% tabs %}
{% tab title="URL" %}
```bash
echo -n "<content>" | jq -sRr @urid
```
{% endtab %}

{% tab title="Base64" %}
```bash
echo -n "<content>" | base64 -d
```
{% endtab %}

{% tab title="Hex" %}
```bash
echo -n "<content>" | xxd -p -r
```
{% endtab %}

{% tab title="Decimal" %}
```bash
echo -n "<content>" | awk '{ for (i=1;i<=NF;i++) printf "%c", $i }'
```
{% endtab %}
{% endtabs %}

&#x20;
