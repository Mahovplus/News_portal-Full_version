from app.error_handlers.page_not_found import not_found
from app.error_handlers.access_denied import no_access
from app.error_handlers.something_wrong import server_error

exception_handlers = {
    404: not_found,
    403: no_access,
    500: server_error
}
