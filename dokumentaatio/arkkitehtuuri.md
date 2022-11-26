# Arkkitehtuuri
## Pakkausrakenne
```mermaid
 classDiagram
      
      services <|-- ui
      objects <|-- services
      repositories <|-- services
      objects <|-- repositories
      
      class ui{
      }
      
      class services{
      }
      
      class repositories{
      }
      
      class objects{
      }
```
