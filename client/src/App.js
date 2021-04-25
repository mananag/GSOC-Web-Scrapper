import MaterialTable from "material-table";
import data from './data/out.json'

function App() {

    return (
        <div>
            <MaterialTable
            title="GSOC Frequency Viewer"
            columns={[
                {title: 'Organizations', field: 'Organizations'},
                {title: 'About', field: 'About'},
                {title: 'Category', field: 'Category'},
                {title: 'Technology', field: 'Technology'},
                {title: 'Topics', field: 'Topics'},
                {title: 'Count', field: 'Count'},
                {title: 'Last Appeared', field: 'Last Appeared'},
            ]}
            data={data}
            options={{
                paging: true,
                pageSize: 20,       // make initial page size
                emptyRowsWhenPaging: true,   //to make page size fix in case of less data rows
                pageSizeOptions: [20, 30, 50],
                exportButton: true// rows selection options
            }}
        />
        </div>

    )
}

export default App;
