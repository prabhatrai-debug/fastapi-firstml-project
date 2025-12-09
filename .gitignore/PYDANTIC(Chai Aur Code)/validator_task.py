


## TODO: Create Booking model

# Fields:

# - user_id: int
# - room_id: int
# - nights: int (must be >=1)
# - rate_per_night: float
# Also, add computed field: total_amount = nights*rate_per_night



from pydantic import BaseModel,computed_field,Field

class Booking(BaseModel):
    user_id:int
    room_id:int
    nights:int=Field(...,gt=1)
    rate_per_night:float


    @computed_field
    @property
    def total_amount(self)->float:
        return self.nights*self.rate_per_night
    
