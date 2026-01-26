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

## URL

{% tabs %}
{% tab title="Encode" %}
```bash
echo -n "<content>" | jq -sRr @uri
```
{% endtab %}

{% tab title="Decode" %}
```bash
echo -n "<content>" | jq -sRr @urid
```
{% endtab %}
{% endtabs %}

## Base64

{% tabs %}
{% tab title="Encode" %}
```bash
echo -n "<content>" | base64 -w 0
```
{% endtab %}

{% tab title="Decode" %}
```bash
echo -n "<content>" | base64 -d
```
{% endtab %}
{% endtabs %}

## Hex

{% tabs %}
{% tab title="Encode" %}
```bash
echo -n "<content>" | xxd -p -c 0
```
{% endtab %}

{% tab title="Decode" %}
```bash
echo -n "<content>" | xxd -p -r
```
{% endtab %}
{% endtabs %}

## PowerShell

{% tabs %}
{% tab title="Base64" %}
```bash
echo -n "<content>" | 
```
{% endtab %}
{% endtabs %}

&#x20;
