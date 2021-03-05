
#!/bin/bash

for i in single double
do
    python3 main.py --total_plate 10 --state Perak --plate_type ${i}
    python3 main.py --total_plate 10 --state Selangor --plate_type ${i}
    python3 main.py --total_plate 10 --state Pahang --plate_type ${i}
    python3 main.py --total_plate 10 --state Kelantan --plate_type ${i}
    python3 main.py --total_plate 10 --state Putrajaya --plate_type ${i}
    python3 main.py --total_plate 10 --state Johor --plate_type ${i}
    python3 main.py --total_plate 10 --state Kedah --plate_type ${i}
    python3 main.py --total_plate 10 --state Malacca --plate_type ${i}
    python3 main.py --total_plate 10 --state 'Negeri Sembilan' --plate_type ${i}
    python3 main.py --total_plate 10 --state Penang --plate_type ${i}
    python3 main.py --total_plate 10 --state Perlis --plate_type ${i}
    python3 main.py --total_plate 10 --state 'Kuala Lumpur(1)' --plate_type ${i}
    python3 main.py --total_plate 10 --state 'Kuala Lumpur(2)' --plate_type ${i}
    python3 main.py --total_plate 10 --state Sarawak --plate_type ${i}
    python3 main.py --total_plate 10 --state Sabah --plate_type ${i}
done
python3 main.py --total_plate 10 --plate_type 'putrajaya'