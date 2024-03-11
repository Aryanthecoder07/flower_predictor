from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class IRISD(BaseModel):
    s_length: float 
    s_width: float 
    p_length: float 
    p_width: float