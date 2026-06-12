
# ROS Haritalandırma ve otonom olarak engellerden kaçarak hedef noktaya gitme

Bu proje ROS Navigation stack kullanarak bir robotun önceden tanımlanmış koordinatlara sırayla gitmesini sağlar. Amaç, actionlib ve move_base kullanarak temel bir otonom navigasyon mantığını öğrenmektir.

## Kullanılan Teknolojiler
- ROS Noetic
- Python 3
- move_base (Actionlib)
- Gazebo + Turtlebot3

## Çalışma Mantığı
Robot, Python scripti içinde tanımlanan waypoint listesine sırayla gönderilir. Her hedef move_base action server’a goal olarak iletilir ve robot hedefe ulaşana kadar beklenir. Hedefe ulaşıldığında bir sonraki noktaya geçilir.

## Waypoint Listesi
Robot aşağıdaki koordinatları ve yönleri sırasıyla ziyaret eder:

- (-0.484, -0.481, 0.00247)
- (0.599, -1.66, 0.00247)
- (1.73, 0.547, 0.00247)
- (-0.518, 1.79, -0.0014)
- (-0.361, 0.51, 0.00845)
- 
## Kurulum

ROS ve Turtlebot3 paketlerinin kurulu olması gerekir.

```bash
sudo apt install ros-noetic-turtlebot3*
````

## Çalıştırma

Gazebo ortamını başlat:

```bash
roslaunch turtlebot3_gazebo turtlebot3_world.launch
```

Navigation sistemini başlat:

```bash
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$(rospack find my_navigation)/maps/my_map.yaml
```

Scripti çalıştır:

```bash
rosrun my_navigation otonom_hedef.py
```

## Notlar

* Robotun doğru çalışması için RViz üzerinden initial pose verilmelidir.
* Waypoint koordinatları haritaya göre ayarlanmıştır.
* Proje eğitim amaçlıdır, optimize edilmemiştir.

## Amaç

ROS Navigation ve MoveBase action yapısını öğrenmek ve temel waypoint navigation mantığını anlamak.
