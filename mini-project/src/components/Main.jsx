import React from 'react'
import "./style/main.scss"

const Main = () => {
  const filterElements = [
    {
      name: 'Brightness'
    },
    {
      name: 'Grayscale'
    },
    {
      name: 'Sepia'
    },
    {
      name: 'Saturate'
    },
    {
      name: 'Contrast'
    },
    {
      name: 'Rotate'
    },
  ]
  return (
    <div className='image_editor'>
      <div className="card">
        <div className="card_header">
          <h2>------ Image Editor ------</h2>
          <div className="card_body">
            <div className="sidebar">
              <div className="sidebody">
                <div className="filter_section">
                  <span>Filter</span>
                  <div className="filter_key">
                    {filterElements.map((v, i) => (
                      <button key={i}> {v.name} </button>
                    ))}
                  </div>
                </div>
                <div className="filter_slider">
                  <div className="label_bar">
                    <label htmlFor="range">Rotate</label>
                    <span>100%</span>
                  </div>
                  <input type="range" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Main