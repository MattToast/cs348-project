import React from 'react';

import ObjectCard from '../components/ObjectCard/ObjectCard';
import NewLocationForm from '../components/Forms/NewLocationForm';
class Locations extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      locationList: []
    }
  }

  componentDidMount() {
    fetch('/api/locations')
      .then(res => res.json())
      .then(data => this.setState({ locationList: data }));
  }

  render() {
    const locs = this.state.locationList;
    return (
      <div>
        <NewLocationForm />
        <div>
          {
            locs.map((loc) => {
              return (<ObjectCard data={loc} />);
            })
          }
        </div>
      </div>
    );
  }
}

export default Locations;
