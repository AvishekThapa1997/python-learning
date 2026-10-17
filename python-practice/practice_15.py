def calculate_average_order_value(total_amount, order_count):
    if order_count <= 0:
        raise ValueError('order_count cannot be less than or equal to zero')
    return total_amount / order_count