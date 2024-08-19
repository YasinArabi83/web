import pytest

from DataProcessor import DataProcessor


def test_data_processor():
    pages = [
        [
            {
                "type": "ad",
                "detail": {
                    "title": "Car 1",
                    "year": "2020",
                    "mileage": "10,000 km",
                    "location": "Location 1",
                    "body_color": "Red"
                },
                "price": {
                    "price": "20,000"
                }
            },
            {
                "type": "ad",
                "detail": {
                    "title": "Car 2",
                    "year": "2019",
                    "mileage": "20,000 km",
                    "location": "Location 2",
                    "body_color": "Blue"
                },
                "price": {
                    "price": "15,000"
                }
            }
        ]
    ]

    processor = DataProcessor(pages)
    result = processor.data_processor()

    expected = [
        {
            "title": "Car 1",
            "year": 2020,
            "mileage": 10000,
            "location": "Location 1",
            "body_color": "Red",
            "price": 20000
        },
        {
            "title": "Car 2",
            "year": 2019,
            "mileage": 20000,
            "location": "Location 2",
            "body_color": "Blue",
            "price": 15000
        }
    ]

    assert result == expected


if __name__ == "__main__":
    pytest.main()
