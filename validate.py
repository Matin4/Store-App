from datetime import datetime

class Validate():      
    def validate_string(self, text_to_validate):
        if isinstance(text_to_validate, str):
            try:
                if int(text_to_validate):
                    return False
                else:
                    return True
            except Exception as e:
                return True
        else:
            return False

    def validate_integer(self, text_to_validate):
        if text_to_validate:
            if isinstance(text_to_validate, int):
                return True
            try:
                return int(text_to_validate)
            except (ValueError, TypeError):
                return False
        else:
            return False
        
    def validate_float(self, text_to_validate):
        if isinstance(text_to_validate, float):
            return True
        try:
            return float(text_to_validate)
        except (ValueError, TypeError):
            return False

    def validate_date(self, text_to_validate, date_format="%Y-%m-%d"):
        if text_to_validate:
            if isinstance(text_to_validate, datetime):
                return True
            if isinstance(text_to_validate, str):
                try:
                    return True # datetime.strptime(text_to_validate, date_format)
                except ValueError:
                    raise ValueError(f"String '{text_to_validate}' is not a valid date (format: {date_format})")
            raise ValueError(f"Cannot convert {text_to_validate} to date")
        else:
            return False
        
    def validate_phone(self, text_to_validate):
        if text_to_validate:
            try:
                if isinstance(text_to_validate, str):
                    if int(text_to_validate):
                        return True
                if isinstance(text_to_validate, int):
                    return True
            except:
                return False